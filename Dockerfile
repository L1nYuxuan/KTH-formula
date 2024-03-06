# 基于Ubuntu 18.04镜像
FROM ubuntu:18.04

# 避免在安装过程中出现交互式提示
ENV DEBIAN_FRONTEND noninteractive

# 安装必要的软件包
RUN apt-get update && apt-get install -y \
    software-properties-common \
    lsb-release \
    gnupg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 添加ROS仓库
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# 添加ROS密钥
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# 安装ROS Melodic
RUN apt-get update && apt-get install -y ros-melodic-desktop-full \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 初始化rosdep
RUN rosdep init \
    && rosdep update

# 设置环境变量
ENV ROS_WS=/root/catkin_ws

# 创建catkin工作空间
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS

# 构建catkin工作空间
RUN /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make'

# 自动源ROS环境
RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc \
    && echo "source $ROS_WS/devel/setup.bash" >> ~/.bashrc

# 设置容器启动时默认执行的命令
CMD ["bash"]
