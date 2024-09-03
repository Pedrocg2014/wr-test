from log_reader import Log, MessageType
import matplotlib.pyplot as plt

class Points:
    def __init__(self) -> None:
        self.x = []
        self.y = []
    def plotgraph(self, name):
        plt.scatter(self.x, self.y)
        plt.scatter(self.x, self.y, color='orange', marker='^', s=1)

        plt.title('Ball Position', fontsize=16, color='blue')
        plt.xlabel('X Axis', fontsize=14)
        plt.ylabel('Y Axis', fontsize=14)

        plt.savefig(name)

#class plotter:
def plotball(message, pball: Points):
    for ball in message.tracked_frame.balls:
        pball.x.append(ball.pos.x)
        pball.y.append(ball.pos.y)
def plotrobots(message, pyellow: Points, pblue: Points):
    for robot in message.tracked_frame.robots:
        if robot.robot_id.team == 1:
            pyellow.x.append(robot.pos.x)
            pyellow.y.append(robot.pos.y)
        elif robot.robot_id.team == 2:
            pblue.x.append(robot.pos.x)
            pblue.y.append(robot.pos.y)



file = "2023-07-06_17-37_OrcaBOT-vs-UBC_Thunderbots.log"
log = Log(file)
pball = Points()
pblue = Points()
pyellow = Points()
referencia = 0
tempo = 0
for l in log:
    type, message = l
    if type == MessageType.MESSAGE_SSL_REFBOX_2013:
        referencia = message.command
    if type == MessageType.MESSAGE_SSL_VISION_TRACKER_2020 and (referencia == 2 or referencia == 3) :
        plotball(message, pball)
        plotrobots(message, pyellow, pblue)


pball.plotgraph("ball.png")
pyellow.plotgraph("yellow.png")
pblue.plotgraph("blue.png")
