function[table]=dropStats(lenght,decay,system,sampling_period)

%%%%%%%%%%%%%%--Given l,epsolon,sampling period--%%%%%%%%%%%%%

l=30;
epsilon = 0.964;
exp_decay= (log(1/epsilon))/l             % desired decay rate from (l,epsilon)
stab=1;                                     % while loop first run
i=1;
cnt=6;
horizon=100;

%%%%%%%%%%% plant %%%%%%%%%%%
A = [-0.313 56.7 0; -0.0139 -0.426 0; 0 56.7 0];
B = [0.232; 0.0203; 0];
C = [0 0 1];
D = [0];  

x0 = [1;1;1];                             % ini state
x = x0;         
t0 = [0];                               
t = t0;
k=0;
n=0;
h = 0.01*30;                                % sampling rate 
open_loop = ss(A,B,C,D);
eig_open= eig(A);                   
Ts=h;
ZOH_open= c2d(open_loop,Ts,'zoh');
[Ap1,Bp1,Cp1,Dp1] = ssdata(ZOH_open);
eig_openZOH=eig(Ap1);   
%    figure(11)
%    step(ZOH_open);
%%%%%%%%%%%%%%%%%%---closed loop---%%%%%%%%%%%%%%%%%%
p = 50000;
Q = p*Cp1'*Cp1;
R = 0.0001;
K = dlqr(Ap1,Bp1,Q,R);

%p=100;
%K= [0.0556 0.3306 0.243];
A1= (Ap1-Bp1*K);
B1=zeros(size(A1,1),1);             %%%--Becomes zero
C1=Cp1;                             %%%--remains same,outputs
D1=Dp1;                             %%%--remains same i.e. zero
closed_loop = ss(A1,B1,C1,D1,Ts);
%    figure(10)
%    step(closed_loop)
eig_closed= eig(A1)
constraints=[];
constraints_di=[];
%%%%%%%%%%%%%%%%%5%%%%--plant with sampling period=m*h --%%%%%%%%%%%%%%%%%%%%%
while (stab==1 && cnt>0)
    m=i;
    Ts=m*h;        
    per_step=Ts/10;
%        time_horizon=30;
    ZOHm= d2d(ZOH_open,Ts,'zoh');
    [Apm,Bpm,Cpm,Dpm] = ssdata(ZOHm);

    Am= (Apm-Bpm*K);
    Bm=zeros(size(Am,1),1);             %%%--Becomes zero
    Cm=Cpm;                             %%%--remains same,outputs
    Dm=Dpm;                             %%%--remains same i.e. zero
    closed_loop = ss(Am,Bm,Cm,Dm,Ts);
    eig_state{i}=eig(Am);

    %%%%%%%%--Contrallability check--%%%%%%%%%%%%
%         p= eig_closed;
%         sp=size(p);
%         p_unique=unique(p);
%         spu=size(p_unique);
%          if(sp(1)>spu(1))
%              for i=1:(sp(1)-spu(1))
%                  p_unique(spu(1)+1)=min(p_unique)-0.11;
%                  spu=size(p_unique);
%              end
%          end
%          eig_closed=p_unique;
    Km=place(Apm,Bpm,eig_closed);      %%--if the controller was designed for mh sampling time        
    closed_m_loop=ss(Apm-Bpm*Km,Bpm,Cpm,Dpm,Ts);  %%--would there be any K possible for stability?
    if(((max(abs(eig(Apm-Bpm*Km)))<1)))
        ifStabilizable(i)=1;                      %%--stabilizable frequency?
        stab=1;
        closed_loops{i}=closed_loop;           
        closed_m_loops{i}=closed_m_loop;
        cnt=cnt-1;
    else
        stab=0;
        fprintf("\n not stabilizable for %dh sampling time",m);
        eig_state{i}=[];
        break;
    end


    %%%--deciding alpha_m for the state--%%%
    if((max(abs(eig_state{i}))<1) && (log(abs(max(eig_state{i})))<exp_decay*(-1)))
        ifStable(i)= 1;            
        fprintf("\n stable for %dh sampling time",m);
%        Alpha(i)=-2.5;        %%--alpha values 
%             Alpha_di(i)=-max(abs(eig_state{i}))^(0.5*i*0.000001);
        Alpha_di(i)=max(abs(eig_state{i}))^2-1;
        Alpha_diBar(i)=1+Alpha_di(i);
    end
    if(max(abs(eig_state{i}))>1)
        ifStable(i)=0;
        fprintf("\n not stable for %dh sampling time",m);
%        Alpha(i)=3.5;           %%--alpha values
%             Alpha_di(i)=max(abs(eig_state{i}))^(0.5);
        Alpha_di(i)=max(abs(eig_state{i}))^2-1;
        Alpha_diBar(i)=1+Alpha_di(i);
    end


    %%%--LMi solution to find out Lyapunov func Slow switching--%%%
%    Pm{i}=sdpvar(size(Am,1),size(Am,1));
    Pm_di{i}=sdpvar(size(Am,1),size(Am,1));
%     Probm=[Am'*Pm{i}+Pm{i}'*Am-Alpha(i)*eye(size(Pm{i}))*Pm{i} zeros(size(Am));
%             zeros(size(Am)) -Pm{i}];

    Probm_di=[Am'*Pm_di{i}*Am-(1+Alpha_di(i))*eye(size(Pm_di{i}))*Pm_di{i} zeros(size(Am));
              zeros(size(Am)) -Pm_di{i}];

%    constraint= Probm <= 0;
    constraint_di= Probm_di <= 0;
%    solvesdp(constraint);
    solvesdp(constraint_di);
%    P{i}=double(Pm{i});               %%--P values for cont sys
    P_di{i}=double(Pm_di{i});           %%--P values for discrete sys
    sampling_time(i)=Ts;            
    i=i+1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% p=1;q=1;
for i=1:size(sampling_time,2)
%    mum{i}=sdpvar(1,1);
    mum_di{i}=sdpvar(1,1);
    for j=1:size(sampling_time,2)
%        constraints=[constraints, P{i}-mum{i}*eye(size(P{j}))*P{j}<= 0,mum{i}>1];
        constraints_di=[constraints_di, P_di{i}-mum_di{i}*eye(size(P_di{j}))*P_di{j}<= 0,mum_di{i}>1];
%         mu(j)=(det(P{i}/P{j})^(1/size(P{i},1)));        
   end
end
%%%%%%%%%%%%--Solving LMI to find out Mu--%%%%%%%%%%%%%%
solvesdp(constraints);
solvesdp(constraints_di);
p=1;q=1;
gammaUnstable=[]
%%%%%%%%%%%--Gamma,Taud calculation--%%%%%%%%%%%%%
for i=1:size(sampling_time,2)
    if (isdt(closed_loops{i})==1)  % for discrete-time
        Mu(i)=double(mum_di{i});
%         Taud(i)= -(log(Mu(i))/log(Alpha_diBar(i)));      %%%%-dwell time for ith state
        Taud(i)= log(Mu(i)/abs(log(Alpha_diBar(i))));      %%%%-dwell time for ith state
        Count(i)= (ceil(Taud(i)/sampling_time(i)));     %%%--Permissible self loop count
         gamma(i)= (Alpha_diBar(i)*((Mu(i))^(1/Taud(i))));
%        gamma(i)= Alpha_di(i)+(log(Mu(i))/Taud(i));
         gamma_eig(i)= max(abs(pole(closed_loops{i})));  %pole(closed_loops{i} is eig_state{i}

        if(ifStable(i))
           gammaStable(p)= (gamma(i));      %%--gamma_plus
 %          gammaStable(p)= (gamma_eig(i));
            p=p+1;
        else
           gammaUnstable(q)=(gamma(i));    %%%--gamma_minus
 %          gammaUnstable(q)= (gamma_eig(i));
            q=q+1;
        end
    end   
end  % end for
%%%%%%%%%%%%%%--Values derived--%%%%%%%%%%%%%%%
if(~isempty(gammaUnstable))
    DwellingRatio= ceil((log(max(gammaUnstable))+(exp_decay))/(-log(max(gammaStable))+(exp_decay)));
    % DwellingRatio= ceil((((max(gammaUnstable)))+(exp_decay))/(((max(gammaStable))))-(exp_decay));
    % T_minus (dwelling time in stable sys)/T_plus (dwelling time in unstable sys)
end

Sampling_Time=sampling_time';
Self_Loop_Count=Count';
Min_Dwell_Time=Taud';
Mu_Val=Mu';
Alpha_val=Alpha_di';
% Gamma=log(gamma_eig');
Gamma=log(gamma');
T=table(Sampling_Time,Self_Loop_Count,Min_Dwell_Time,Mu_Val,Alpha_val,Gamma)

%DwellingRatio
%rate
exp_decay