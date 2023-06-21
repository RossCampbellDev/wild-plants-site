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

function addTag() {
    var tagTextInput = document.getElementById("tags-input-form");
    tagTextInput.style.display = "block";
}

function completeAddTag() {
    const tagTextNew = document.getElementById("new-tag-input");
    const tag = tagTextNew.value;
    const tagTextArea = document.getElementById("tags-input-text");

    const regex = /^[a-zA-Z0-9]+$/;

    if (regex.test(tag)) {
        if (tagTextArea.value == "") {
            tagTextArea.value = tagTextArea.value + "#" + tag.replace("#","").replace(" ", "");
        } else {
            tagTextArea.value = tagTextArea.value + " #" + tag.replace("#","").replace(" ", "");
        }

        tagTextNew.value = "";

        const tagTextInput = document.getElementById("tags-input-form");
        tagTextInput.style.display = "none";
    } else {
        alert("Only numbers and letters please!");
        tagTextNew.value = "";
    }
}

function cancelAddTag() {
    const tagTextNew = document.getElementById("new-tag-input");
    tagTextNew.value = "";
    const tagTextInput = document.getElementById("tags-input-form");
    tagTextInput.style.display = "none";
}

function showNote(title,date,desc,tags) {
    const f = document.getElementById("popup-input-form");
    const t = document.getElementById("popup-input-title");
    const txt = document.getElementById("review-note-text");
    const tgs = document.getElementById("review-note-tags");
    f.style.display = 'block';
    t.innerHTML = title + "<br/>" + date;
    txt.innerHTML = desc;
    tgs.innerHTML = tags;
}

function closeNote() {
    const f = document.getElementById("popup-input-form");
    f.style.display = 'none';
}