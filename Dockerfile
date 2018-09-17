FROM amazonlinux:1
RUN yum -y update
RUN yum install -y httpd24 \
        php70 \
        zlib-devel \
        bzip2 \
        bzip2-devel \
        readline-devel \
        sqlite \
        sqlite-devel \
        openssl-devel \
        git
EXPOSE 80 8080 22 8888 7777
RUN mkdir -p /var/www/html/HealthCheck
COPY . /var/www/html/HealthCheck
COPY . /var/www/html/
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    eval "$(pyenv init -)"
RUN pyenv install anaconda3-5.1.0
RUN pyenv global anaconda3-5.1.0
ENV PATH $PYENV_ROOT/versions/anaconda3-5.1.0/bin/:$PATH
RUN conda update conda -y
RUN conda update anaconda -y
RUN mkdir ~/tensorflow
RUN cd ~/tensorflow/
RUN pip install --upgrade pip
RUN conda create -n tensorflow pip python=3.6
RUN source activate tensorflow
RUN git clone https://github.com/tensorflow/tensorflow.git ~/tensorflow/
RUN pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.10.1-cp36-cp36m-linux_x86_64.whl
RUN echo '#!/bin/bash' >> ~/jupyter_tsb.sh
RUN echo 'python ~/tensorflow/tensorflow/examples/tutorials/mnist/mnist_with_summaries.py' >> ~/jupyter_tsb.sh
RUN echo '(nohup jupyter notebook --port 8888 --allow-root --no-browser --ip=* --NotebookApp.token="Lissandra-1"; tensorboard --logdir=/tmp/ --port 7777) > ~/nohup.out 2>&1' >> ~/jupyter_tsb.sh
RUN chmod +x ~/jupyter_tsb.sh
CMD /etc/init.d/httpd start && \
    sh ~/jupyter_tsb.sh && \
    sleep 4