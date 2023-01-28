const operation = document.getElementsByName('operation');
const input_method = document.getElementsByName('input_method');

// chage msg type based on input method
input_method.forEach((im) => {
    im.addEventListener('change', () => {
        const msg_file = document.getElementById('msg-file');
        const msg_text = document.getElementById('msg-text');
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