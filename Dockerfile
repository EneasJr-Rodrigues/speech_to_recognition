ARG base_image
FROM $base_image

ARG config_path

ARG jfrog_user
ARG jfrog_pass

LABEL maintainer="eneas.rodrigues25@gmail.com"
USER $root
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

## install image of python 3 last version
RUN python -m pip install --root --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt
# ubuntu
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev gcc -y
#RUN apt-get install openjdk-11-jdk
RUN pip install pyaudio
RUN pip install pydub
RUN pip install --upgrade setuptools
RUN pip install jupyterlab
RUN python -m spacy download pt_core_news_sm
RUN pip install nltk
RUN python -c "import nltk; nltk.download('stopwords')"
RUN python -c "import nltk; nltk.download('punkt')"

# NbEtensions
RUN python -m pip install --upgrade jupyterthemes
RUN python -m pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable contrib_nbextensions_help_item/main
RUN jupyter nbextension enable autosavetime/main
RUN jupyter nbextension enable freeze/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable toc2/main


RUN echo 'c.NotebookApp.contents_manager_class = "notedown.NotedownContentsManager"' >> ~/.jupyter/jupyter_notebook_config.py