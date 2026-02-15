
// This file contains the JavaScript code for the website. 
// It is responsible for handling the delete note functionality 
// of the website.

function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}   