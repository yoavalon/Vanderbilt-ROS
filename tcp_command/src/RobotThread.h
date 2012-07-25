#ifndef ___ROBOTTHREAD_H___
#define ___ROBOTTHREAD_H___

#include <QThread>
#include <QObject>
#include <QStringList>
#include <stdlib.h>
#include <iostream>
#include "assert.h"

#include <ros/ros.h>
#include <ros/network.h>
#include <std_msgs/String.h>

namespace server {
class RobotThread : public QThread {
	Q_OBJECT
public:
    RobotThread(int argc, char **pArgv);
    virtual ~RobotThread();
    bool init();
	void SetSpeed(double speed, double angle);
    void setCommand(QString cmd);
    void run();

private:
    QString command;
	
    int m_Init_argc;
    char** m_pInit_argv;

    ros::Publisher cmd_publisher;
	/** a position 2d proxy */

	
};
}//end namespace
#endif
