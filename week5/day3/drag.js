document.querySelector('#upload').addEventListener('dragover', function(e) {
    e.preventDefault();
    console.log('dragenter');
    this.style.background = 'blue';
});



document.querySelector('#upload').addEventListener('dragleave', function(e) {
    e.preventDefault();
    console.log('dragenter');
    this.style.background = 'white';
});


document.querySelector('#upload').addEventListener('drop', function(e) {
    e.preventDefault();
    alert(e.dataTransfer.files[0].name);
});
