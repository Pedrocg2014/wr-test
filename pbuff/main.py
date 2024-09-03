from log_reader import Log, MessageType
import matplotlib.pyplot as plt

file = "2024-07-18_09-02_GROUP_PHASE_ITAndroids-vs-Delft_Mercurians.log"
log = Log(file)

x = []
y = []

for l in log:
    t, m = l
    
    if t == MessageType.MESSAGE_SSL_VISION_TRACKER_2020:
        for ball in m.tracked_frame.balls:
            x.append(ball.pos.x)
            y.append(ball.pos.y)

plt.scatter(x, y)
plt.scatter(x, y, color='orange', marker='^', s=1)

plt.title('Ball Position', fontsize=16, color='blue')
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)

plt.show()