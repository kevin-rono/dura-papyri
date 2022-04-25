$('#image').click(function (e){
    var x = e.pageX - this.offsetLeft;
    var y = e.pageY - this.offsetTop;

    alert("clicked");
    
    console.log(x);
}

);