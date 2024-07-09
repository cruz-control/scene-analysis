FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

RUN apt-get update \
    && apt-get --assume-yes upgrade \
    && apt-get clean

RUN apt-get install -y git wget ffmpeg vim make

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-py38_23.11.0-2-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-py38_23.11.0-2-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py38_23.11.0-2-Linux-x86_64.sh 

# mtr environment 
RUN conda --version
RUN conda init
RUN conda create -yn "mtr" python=3.8 \
    && conda install -yn "mtr" pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
RUN conda install -yn "mtr" -c conda-forge tensorboardX easydict tensorflow 
RUN conda install -yn "mtr" -c conda-forge pyyaml scikit-image tqdm numpy
RUN /bin/bash -c "source activate mtr" \
    && pip install waymo-open-dataset-tf-2-11-0

SHELL ["conda", "run", "-n", "mtr", "/bin/bash", "-c"]
