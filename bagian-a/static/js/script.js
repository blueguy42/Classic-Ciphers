const operation = document.getElementsByName('operation');
const input_method = document.getElementsByName('input_method');
const msg_file = document.getElementById('msg-file');
const msg_text = document.getElementById('msg-text');

// chage msg type based on input method
input_method.forEach((im) => {
    im.addEventListener('change', () => {
        if (im.value === 'file') {
            msg_file.style.display = 'block';
            msg_text.style.display = 'none';
        } else {
            msg_file.style.display = 'none';
            msg_text.style.display = 'block';
        }
    });
});

// change msg label to plaintext or ciphertext, if operation is encrypt or decrypt
operation.forEach((op) => {
    op.addEventListener('change', () => {
        const msg_label = document.getElementById('msg-label');
        msg_label.innerText = op.value === 'encrypt' ? 'Plaintext' : 'Ciphertext';
    });
});

// FILE BYTECODE
// const msg_file = document.getElementById('msg-file');
// msg_file.addEventListener('change', () => {
//     const file = msg_file.files[0];
//     const reader = new FileReader();
//     reader.onload = (e) => {
//         console.log(e.target.result);
//     }
//     reader.readAsText(file);
// });

document.getElementsByName("show").forEach((item) => {
    item.addEventListener("change", (e) => {
        if (e.target.value == "without-space") {
            document.getElementById("without-space-result").style.display = "block";
            document.getElementById("group-of-5-result").style.display = "none";
        } else {
            document.getElementById("without-space-result").style.display = "none";
            document.getElementById("group-of-5-result").style.display = "block";
        }
    });
});

// buat vigenere
const type = document.getElementsByName("type");
type.forEach((item) => {
    item.addEventListener("change", (e) => {
        if (e.target.value == "standard" || e.target.value == "autokey") {
            document.getElementById("input-file-container").style.display = "block";
            document.getElementById("input-manual-container").style.display = "block";
        } else {
            document.getElementById("input-file-container").style.display = "block";
            document.getElementById("input-manual-container").style.display = "none";
            document.getElementById("file").checked = true;
            document.getElementById("manual").checked = false;
            msg_file.style.display = 'block';
            msg_text.style.display = 'none';
        }
    });
});