$(document).ready(function() {
    // Замість document.getElementById використовуйте jQuery для отримання елементів DOM.
    var markSelect = $("#mark");
    var modelSelect = $("#model");

    markSelect.on("change", function () {
        var selectedMark = $(this).val();
        if (selectedMark === "") {
            modelSelect.html('<option value="" disabled selected>Select Model</option>');
            modelSelect.prop("disabled", true);
            return;
        }
        fetch(`/get_models/${selectedMark}`)
            .then(response => response.json())
            .then(data => {
                updateModelSelect(data);
            })
            .catch(error => console.error('Error fetching models:', error));
    });

    function updateModelSelect(models) {
        modelSelect.html('<option value="" disabled selected>Select Model</option>');
        models.forEach(function(model) {
            var option = $('<option>', { value: model.id, text: model.name });
            modelSelect.append(option);
        });
        modelSelect.prop("disabled", false);
    }
});


$(document).ready(function() {
    var imageInput = $("#image");
    var previewImage = $("#preview-image");
    var removeImage = $("#remove-image");
    var imagePreview = $("#image-preview");
    var uploadButton = $("#upload-button");

    imageInput.on("change", function() {
        var file = this.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                previewImage.attr("src", e.target.result);
                imagePreview.css("display", "block");
            };
            reader.readAsDataURL(file);
        }
    });

    removeImage.on("click", function() {
        imageInput.val(null);
        previewImage.attr("src", "");
        imagePreview.css("display", "none");
    });

    uploadButton.on("click", function() {
        imageInput.click();
    });
});



// Функція оновлення параметрів пошуку і відправлення форми
function submitForm() {
    document.getElementById("search-form").submit();
}

// Функція оновлення вибору моделі при зміні марки
function updateModelOptions() {
    var markSelect = document.getElementById('mark');
    var modelSelect = document.getElementById('selected_model');
    var selectedMark = markSelect.value;

    if (!selectedMark) {
        modelSelect.selectedIndex = 0; // Скидаємо вибір моделі на "Виберіть модель"
        submitForm(); // Оновлюємо форму після скидання вибору моделі
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var markSelect = document.getElementById('mark');
    var modelSelect = document.getElementById('selected_model');

    markSelect.addEventListener('change', function () {
        var selectedMark = markSelect.value;
        var selectedModel = modelSelect.value;

        // Змінюємо значення моделі на "Виберіть модель" при зміні марки
        modelSelect.selectedIndex = 0;

        // Оновлюємо форму
        submitForm();
    });

    // Викликаємо функцію для початкового стану
    updateModelOptions();
});



