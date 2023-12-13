% Number of Rows of the grid
numRows(NumRows) :- NumRows = #count{X : init(object(node, NodeID), value(at, pair(X, Y)))}.

% Number of Columns of the grid
numColumns(NumColumns) :- NumColumns = #count{Y : init(object(node, NodeID), value(at, pair(X, Y)))}.

% Number of Nodes
numNodes(NumNodes) :- NumNodes = #count{NodeID : init(object(node, NodeID), value(at, pair(X, Y)))}.

% Number of Shelves
numShelves(NumShelves) :- NumShelves = #count{ShelfID : init(object(shelf, ShelfID), value(at, pair(X, Y)))}.

% Number of Products
numProducts(NumProducts) :- NumProducts = #count{ProductID : init(object(product, ProductID), value(on, pair(X, Y)))}.

% Number of Picking Stations
numPickingStations(NumPickingStations) :- NumPickingStations = #count{PSID : init(object(pickingStation, PSID), value(at, pair(X, Y)))}.

% Number of Orders
numOrders(NumOrders) :- NumOrders = #count{OrderID : init(object(order, OrderID), value(pickingStation, PSID))}.

% Number of Robots
numRobots(NumRobots) :- NumRobots = #count{RobotID : init(object(robot, RobotID), value(at, pair(X, Y)))}.

nodeAt(NodeID, pair(X, Y)) :- init(object(node, NodeID), value(at, pair(X, Y))).
pair(X, Y) :- init(object(node, NodeID), value(at, pair(X, Y))).
node(NodeID) :- init(object(node, NodeID), value(at, pair(X, Y))).

highway(HighwayID) :- init(object(highway, HighwayID), value(at, pair(X, Y))).

pickingStationAt(PSID, NodeID) :- init(object(pickingStation, PSID), value(at, pair(X, Y))), init(object(node, NodeID), value(at, pair(X, Y))).
pickingStation(PSID) :- init(object(pickingStation, PSID), value(at, pair(X, Y))), init(object(node, NodeID), value(at, pair(X, Y))).

robotAt(RobotID, object(node, NodeID), 0) :- init(object(robot, RobotID), value(at, pair(X, Y))), nodeAt(NodeID, pair(X, Y)).
robot(RobotID) :- init(object(robot, RobotID), value(at, pair(X, Y))).

shelfOn(ShelfID, object(node, NodeID), 0) :- init(object(shelf, ShelfID), value(at, pair(X, Y))), nodeAt(NodeID, pair(X, Y)).
shelf(ShelfID) :- init(object(shelf, ShelfID), value(at, pair(X, Y))).

productOn(ProductID, object(shelf, ShelfID), with(quantity, Quantity), 0) :- init(object(product, ProductID), value(on, pair(ShelfID, Quantity))).
product(ProductID) :- init(object(product, ProductID), value(on, pair(ShelfID, Quantity))).

orderAt(OrderID, object(node, NodeID), contains(ProductID, Quantity), 0) :- init(object(order, OrderID), value(pickingStation, PickingStationID)), pickingStationAt(PickingStationID, NodeID), init(object(order, OrderID), value(line, pair(ProductID, Quantity))).
order(OrderID) :- init(object(order, OrderID), value(pickingStation, PickingStationID)).

#const n=50.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%    GENERATING ACTIONS     %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

move(0, 1; 0, -1; -1, 0; 1, 0).

{robotMove(RobotID, move(DX, DY), TimeStep) : move(DX, DY)} 1 :- RobotID=1..NumRobots, numRobots(NumRobots), TimeStep=0..TimeSteps, TimeSteps=n-1.
{pickUpShelf(RobotID, ShelfID, TimeStep) : shelf(ShelfID)} 1 :- RobotID=1..NumRobots, numRobots(NumRobots), TimeStep=0..TimeSteps, TimeSteps=n-1.
{putDownShelf(RobotID, ShelfID, TimeStep) : shelf(ShelfID)} 1 :- RobotID=1..NumRobots, numRobots(NumRobots), TimeStep=0..TimeSteps, TimeSteps=n-1.
{deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep) : orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity), TimeStep), productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity), TimeStep), DeliveryQuantity=1..ShelfQuantity} 1 :- RobotID=1..NumRobots, numRobots(NumRobots), TimeStep=0..TimeSteps, TimeSteps=n-1.

% converting them to the necessary output
occurs(object(robot, RobotID), move(DX, DY), TimeStep) :- robotMove(RobotID, move(DX, DY), TimeStep).
occurs(object(robot, RobotID), pickup, TimeStep) :- pickUpShelf(RobotID, _, TimeStep).
occurs(object(robot, RobotID), putdown, TimeStep) :- putDownShelf(RobotID, _, TimeStep).
occurs(object(robot, RobotID), deliver(OrderID, ProductID, DeliveryQuantity), TimeStep) :- deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%    ACTION CONSTRAINTS     %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Two actions cannot occur at the same time
:- occurs(object(robot, RobotID), Action1, TimeStep), occurs(object(robot, RobotID), Action2, TimeStep), Action1 != Action2.

%%%%%%%%%%%%        ROBOT MOVING        %%%%%%%%%%%%
% Robot cannot move outside of the grid
:- robotAt(RobotID, object(node, NodeID), TimeStep), robotMove(RobotID, move(DX, DY), TimeStep), nodeAt(NodeID, pair(X, Y)), X+DX < 1.
:- robotAt(RobotID, object(node, NodeID), TimeStep), robotMove(RobotID, move(DX, DY), TimeStep), nodeAt(NodeID, pair(X, Y)), Y+DY < 1.
:- robotAt(RobotID, object(node, NodeID), TimeStep), robotMove(RobotID, move(DX, DY), TimeStep), nodeAt(NodeID, pair(X, Y)), X+DX > NumColumns, numColumns(NumColumns).
:- robotAt(RobotID, object(node, NodeID), TimeStep), robotMove(RobotID, move(DX, DY), TimeStep), nodeAt(NodeID, pair(X, Y)), Y+DY > NumRows, numRows(NumRows).


%%%%%%%%%%%%      PICKING UP SHELF      %%%%%%%%%%%%
% A shelf can't be picked up by 2 robots
:- 2{pickUpShelf(RobotID, ShelfID, TimeStep) : robot(RobotID)}, shelf(ShelfID).

% A robot cannot pick up a shelf if it already has one.
:- pickUpShelf(RobotID, Shelf1, TimeStep), shelfOn(Shelf2, object(robot, RobotID), TimeStep).

% A robot cannot pick up a shelf if a shelf is already on a robot
:- pickUpShelf(Robot1, Shelf, TimeStep), shelfOn(Shelf, object(robot, Robot2), TimeStep).

% A robot can pick up a shelf only if it is on the node containing that shelf
:- pickUpShelf(RobotID, Shelf, TimeStep), shelfOn(Shelf, object(node, NodeID), TimeStep), not robotAt(RobotID, object(node, NodeID), TimeStep).


%%%%%%%%%%%%     PUTTING DOWN SHELF     %%%%%%%%%%%%
% A shelf can't be put down by 2 robots
:- 2{putDownShelf(RobotID, ShelfID, TimeStep) : robot(RobotID)}, shelf(ShelfID).

% A robot can put down a shelf only if it has one.
:- putDownShelf(RobotID, Shelf, TimeStep), not shelfOn(Shelf, object(robot, RobotID), TimeStep).

% A robot cannot put down a shelf on a highway
:- putDownShelf(RobotID, Shelf, TimeStep), robotAt(RobotID, object(node, NodeID), TimeStep), highway(NodeID). 


%%%%%%%%%%%%         DELIVERING         %%%%%%%%%%%%

% Can only deliver if robot is on picking station
:- deliver(RobotID, OrderID, with(_, ProductID, _), TimeStep), orderAt(OrderID, object(node, NodeID), contains(ProductID, _), TimeStep), not robotAt(RobotID, object(node, NodeID), TimeStep).

% Can only deliver if robot has the shelf containing the product
:- deliver(RobotID, OrderID, with(ShelfID, ProductID, _), TimeStep), productOn(ProductID, object(shelf, ShelfID), with(quantity, _), TimeStep), not shelfOn(ShelfID, object(robot, RobotID), TimeStep).

% Cannot deliver more quantities than the order.
:- deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep), orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity), TimeStep), DeliveryQuantity > OrderQuantity.

% Cannot deliver more quantities than the product.
:- deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep), productOn(ProductID, object(shelf, ShelfID), with(quantity, ProductQuantity), TimeStep), DeliveryQuantity > ProductQuantity.




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%    STATES CONSTRAINTS     %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Picking Station cannot be a highway
:- pickingStationAt(_, NodeID), highway(NodeID).

% Shelf cannot be on a highway.
:- shelfOn(Shelf, object(node, NodeID), _), highway(NodeID).

%%%%%%%%%%%%        ROBOT        %%%%%%%%%%%%
% No robot on 2 nodes
:- 2{robotAt(RobotID, object(node, NodeID), TimeStep) : node(NodeID)}, robot(RobotID), TimeStep=0..n.

% No 2 robots on the same node
:- 2{robotAt(RobotID, object(node, NodeID), TimeStep) : robot(RobotID)}, node(NodeID), TimeStep=0..n.

% Robots can't swap places
:- robotAt(Robot1, object(node, Node1), TimeStep), robotAt(Robot1, object(node, Node2), TimeStep+1), robotAt(Robot2, object(node, Node2), TimeStep), robotAt(Robot2, object(node, Node1), TimeStep+1), Robot1 != Robot2.


%%%%%%%%%%%%        SHELF        %%%%%%%%%%%%

% No shelf on 2 robots
:- 2{shelfOn(Shelf, object(robot, RobotID), TimeStep) : robot(RobotID)}, shelf(Shelf), TimeStep=0..n.

% No 2 shelves on the same robot
:- 2{shelfOn(Shelf, object(robot, RobotID), TimeStep) : shelf(Shelf)}, robot(RobotID), TimeStep=0..n.

% No shelf on 2 nodes
:- 2{shelfOn(Shelf, object(node, NodeID), TimeStep) : node(NodeID)}, shelf(Shelf), TimeStep=0..n.

% No 2 shelves on the same node
:- 2{shelfOn(Shelf, object(node, NodeID), TimeStep) : shelf(Shelf)}, node(NodeID), TimeStep=0..n.

% No shelf on 2 locations (robot, node)
:- shelfOn(Shelf, object(node, _), TimeStep), shelfOn(Shelf, object(robot, _), TimeStep).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%      ACTIONS EFFECTS      %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Effect of moving a robot
robotAt(RobotID, object(node, NewNodeID), TimeStep+1) :- robotAt(RobotID, object(node, NodeID), TimeStep), nodeAt(NodeID, pair(X, Y)), nodeAt(NewNodeID, pair(X+DX, Y+DY)), robotMove(RobotID, move(DX, DY), TimeStep).

% Effect of picking up a shelf
shelfOn(Shelf, object(robot, RobotID), TimeStep+1) :- pickUpShelf(RobotID, Shelf, TimeStep), shelfOn(Shelf, object(node, NodeID), TimeStep), robotAt(RobotID, object(node, NodeID), TimeStep).

% Effect of putting down a shelf
shelfOn(Shelf, object(node, NodeID), TimeStep+1) :- putDownShelf(RobotID, Shelf, TimeStep), shelfOn(Shelf, object(robot, RobotID), TimeStep), robotAt(RobotID, object(node, NodeID), TimeStep).

% Effect of delivering a product
orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity - DeliveryQuantity), TimeStep+1) :- deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep), orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity), TimeStep).
productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity - DeliveryQuantity), TimeStep+1) :- deliver(RobotID, OrderID, with(ShelfID, ProductID, DeliveryQuantity), TimeStep), productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity), TimeStep).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%      LAW OF INERTIA       %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

robotAt(RobotID, object(node, NodeID), TimeStep+1) :- robotAt(RobotID, object(node, NodeID), TimeStep), not robotMove(RobotID, move(_, _), TimeStep), TimeStep < n.
shelfOn(Shelf, object(node, NodeID), TimeStep+1) :- shelfOn(Shelf, object(node, NodeID), TimeStep), not pickUpShelf(_, Shelf, TimeStep), TimeStep < n.
shelfOn(Shelf, object(robot, RobotID), TimeStep+1) :- shelfOn(Shelf, object(robot, RobotID), TimeStep), not putDownShelf(RobotID, Shelf, TimeStep), TimeStep < n.
orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity), TimeStep+1) :- orderAt(OrderID, object(node, NodeID), contains(ProductID, OrderQuantity), TimeStep), productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity), TimeStep), not deliver(_, OrderID, with(ShelfID, ProductID, _), TimeStep), TimeStep < n.
productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity), TimeStep+1) :- productOn(ProductID, object(shelf, ShelfID), with(quantity, ShelfQuantity), TimeStep), not deliver(_, _, with(ShelfID, ProductID, _), TimeStep), TimeStep < n.

% Goal state
:- not orderAt(OrderID, object(node, _), contains(ProductID, 0), n), orderAt(OrderID, object(node, _), contains(ProductID, _), 0).

numActions(NumActions) :- NumActions = #sum{1, O, A, TimeStep : occurs(O, A, TimeStep)}.
timeTaken(N-1) :- N = #count{TimeStep : occurs(_, _, TimeStep)}.
#minimize{1, O, A, TimeStep : occurs(O, A, TimeStep)}.
#minimize{TimeStep : occurs(_, _, TimeStep)}.

%#show node/1.
%#show robot/1.
%#show shelf/1.
%#show product/1.
%#show order/1.
%#show nodeAt/2.
%#show robotAt/3.
%#show shelfOn/3.
%#show productOn/4.
%#show orderAt/4.

%#show robotMove/3.

#show occurs/3.
#show numActions/1.
#show timeTaken/1.