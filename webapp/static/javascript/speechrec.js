function startDictation() {

  if (window.hasOwnProperty('webkitSpeechRecognition')) {

    var recognition = new webkitSpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.lang = "en-US";
    recognition.start();
    /*
    var cur_value = "";
    recognition.onspeechend = function(e) {
      cur_value = document.getElementById('textbox').value + "**";
    };
    recognition.onspeechstart = function(e) {
      document.getElementById('textbox').value = cur_value;
    };
    */
    recognition.onresult = function(e) {
      document.getElementById('textbox').value
                               = e.results[0][0].transcript;
      //recognition.stop();
    };

    recognition.onerror = function(e) {
      recognition.stop();
    }

  }
}
