FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update

###############################################################################
###############################################################################
#                             Common dependencies                             #
###############################################################################
###############################################################################

# Install Poky dependencies
RUN apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
    build-essential chrpath socat cpio python3 python3-pip python3-pexpect \
    xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa \
    libsdl1.2-dev xterm python3-subunit mesa-common-dev rsync zstd file \
    liblz4-tool

# Install common utils
RUN apt-get install -y git zip nano screen tree curl sudo flex bison libncurses-dev tzdata graphviz

RUN mkdir -p /opt/repo
RUN curl https://storage.googleapis.com/git-repo-downloads/repo > /opt/repo/repo
RUN chmod a+rx /opt/repo/repo

# Set utf-8 locale for Poky
RUN apt-get install -y locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# Fix timezone (/etc/localtime) config
ENV TZ 'Europe/Kyiv'
RUN echo $TZ > /etc/timezone && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# RUN useradd -ms /bin/bash pokyuser
#RUN adduser --disabled-password --gecos '' pokyuser
#RUN adduser pokyuser sudo
#RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


ARG host_uid=1001
ARG host_gid=1001
RUN groupadd -g 1000 dev \
            && useradd -u 1000 -g dev -d /home/dev dev \
            && mkdir /home/dev \
            && chown -R dev:dev /home/dev

###############################################################################
###############################################################################
#                           Yocto general dependencies                        #
###############################################################################
###############################################################################

ENV YOCTO_RELEASE=kirkstone
# USER pokyuser
# # Set default git credentials
RUN git config --global user.name "pokyuser"
RUN git config --global user.email "pokyuser@example.com"

WORKDIR /
RUN rm -rf poky/
# It is redundand, due to NXP repo contains pinned version of poky as submodule
RUN git clone git://git.yoctoproject.org/poky -b $YOCTO_RELEASE
# RUN pip3 install -r /poky/bitbake/toaster-requirements.txt

WORKDIR /poky
RUN mkdir /poky/build

RUN git clone https://github.com/agherzan/meta-raspberrypi -b $YOCTO_RELEASE
RUN git clone https://github.com/openembedded/meta-openembedded.git -b $YOCTO_RELEASE
RUN git clone https://github.com/meta-qt5/meta-qt5.git -b $YOCTO_RELEASE
# COPY meta-custom /poky/meta-custom
# COPY meta-image-config /poky/meta-image-config
# COPY custom-images/ /poky/custom-images


RUN chown -R dev:dev /poky

# USER dev
WORKDIR /poky/

