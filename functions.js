function At() {
    alert("surprise!!");
}

function AK() {
    var yes = confirm('你確定嗎？');
    if (yes) {
        alert('你按了確定按鈕');
    } else {
        alert('你按了取消按鈕');
    }
}

function ShowFocus() {
    document.getElementById('ShowBox').innerHTML = '欄位已經被 Focus';
}

function pressed() {
    document.getElementsByClassName("btn").click();
}

function LOL() {
    window.open(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )
}

function changecolor1() {
    document.getElementById("bg").style.backgroundColor = "#F00";
}

function changesize() {
    document.getElementsByClassName("btn").style.width = "200px";
    ocument.getElementsByClassName("btn").style.height = "200px";
}