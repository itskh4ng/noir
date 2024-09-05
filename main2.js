javascript:(function(){
  fetch('https://raw.githubusercontent.com/itskh4ng/noir/main/engine.js')
    .then(response => response.text())
    .then(scriptContent => {
      eval(scriptContent);
    })
    .catch(error => alert('Error loading script: ' + error));
})();
