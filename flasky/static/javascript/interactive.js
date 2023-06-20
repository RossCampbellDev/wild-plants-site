function minimise(who) {
    var blockElement = who.parentNode.children[1];
    if (blockElement.style.display === "none") {
        who.textContent = "[-]";
        blockElement.style.display = "block";
    } else {
        who.textContent = "[+]";
        blockElement.style.display = "none";
    }
}