function startDictation(cur_value) {

  if (window.hasOwnProperty('webkitSpeechRecognition')) {

    var recognition = new webkitSpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function(e) {
      document.getElementById('textbox').value
                               = cur_value + " " + e.results[0][0].transcript;
      //recognition.stop();
    };

    recognition.onerror = function(e) {
      recognition.stop();
    }

  }
}
