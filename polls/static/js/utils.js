function file_to_preview(input, img) {
    var file_reader = new FileReader();
    var file = input.files[0];
    
    file_reader.onloadend = function () {
        img.src = file_reader.result;
    }

    if (file) {
        file_reader.readAsDataURL(file);
    }
    else {
        img.src = "";
    }
}