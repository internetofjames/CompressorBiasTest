# CompressorBiasTest
A web app built with Flask that performs and collects data for a perceptual audio experiment.

Created during a busy time in my college career, will update README with functionality later.

Current issues:
  The questions.py blueprint has a separate function for each webpage, instead of a modular system. Each function passes
  the input values to the HTML template for some "modularity". However, grabbing the audio files for each current question
  is completely dependent on the .DS_Store file residing in the first indicie of the flaskr/static/audio directory.
