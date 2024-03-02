% IE630M Assignment
% Roll no.: 190260039	Name: Shah Heetak Jayesh 
% Roll no.: 19D100011	Name: Modi Shivkumar Ashokbhai		
% Topic 1	Option A and B

function [mean_cost] = project_ab(M, L, n)    % Takes input as M (the maximum inventory level), L (the reorder point) and no. of replications you want
                                              % Gives output of mean cost of each replication i.e. yi_bar
infinity = 10000000000;
lambda = 15;
orderCost = 60;
costOfItem = 5;
rushOrderCost = 120;
rushCostOfItem = 12;
mean_cost = [];
for j=1:n
    i = M;
    t0 = 0;
    t1 = infinity;
    t2 = infinity;
    X = exprnd(1/lambda);
    t3 = t0 + (round(100*X));
    Y = rand;
    q1 = 0;
    q2 = 0;
    cost = 0;
    if Y < 0.5 || Y == 0.5
        demand = 1;
    end
    if Y > 0.5 && (Y < 0.75 || Y == 0.75)
        demand = 2;
    end
    if Y > 0.75 && (Y < 0.875 || Y == 0.875)
        demand = 3;
    end
    if Y > 0.875 && (Y < 1 || Y == 1)
        demand = 4;
    end
    %disp(t3)
    %disp(demand)  
    for t0=0:11200              % 1 unit time is 0.01 month
        if t0 == 1200
            cost = 0;
            %cost1 = cost1 + (cost - cost2);
            %disp(cost1)
            %disp(cost - cost2)
        end
        if t0 == t1
            %disp(i)
            i = (i + q1);
            q1 = 0;
            t1 = infinity;
        end
        if t0 == t2
            %disp(i)
            i = i + q2;
            q2 = 0;
            t2 = infinity;
        end
        if t0 == t3
            if i < demand
                i = i - demand;
                cost = cost - (i*4);
            end
            if i > demand || i == demand
                i = i - demand;
            end
            X = exprnd(1/lambda);
            if X < 0.01
                t3 = t0 + 1;
            end
            if X >= 0.01
                t3 = t0 + (round(100*X));
            end
            Y = rand;
            if Y < 0.5 || Y == 0.5
                demand = 1;
            end
            if Y > 0.5 && (Y < 0.75 || Y == 0.75)
                demand = 2;
            end
            if Y > 0.75 && (Y < 0.875 || Y == 0.875)
                demand = 3;
            end
            if Y > 0.875 && (Y < 1 || Y == 1)
                demand = 4;
            end 
        end
        if mod(t0,100) == 0
            %disp(i)
            if i < 0 || i == 0
                Y = rand;
                %disp(Y)
                Y = Y*0.15;
                t1 = t0 + 100*(round(Y,2) + 0.1);
                q1 = M - i;
                cost = cost + rushOrderCost + (rushCostOfItem * q1);
            end
            if i < L && q1 == 0
                Y = rand;
                %disp(Y)
                t2 = t0 + 100*(round(Y,2) + 0.25);
                q2 = M - i;
                cost = cost + orderCost + (costOfItem * q2);
            end
            cost = cost + i;         %Holding Cost.
        end
    end
    mean_cost(end+1) = cost/100;
end
end