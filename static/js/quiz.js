const url = window.location.href;
const examBox = document.getElementById('exam-box');

$.ajax({
    type: 'GET',
    url: url + 'data',
    success: function (response) {
        console.log(response);
        const data = response.data;
        data.forEach(element => {
            for (const [question, answer] of Object.entries(element)) {
                examBox.innerHTML += '<hr> <div class="mb-2"><b>' + question + '</b></div>'
                answer.forEach(answer => {
                    examBox.innerHTML += '<div class="form-check"><input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1"><label class="form-check-label" for="exampleRadios1">' + answer + '</label></div>'
                });
            }
        });
    },
    error: function (error) {
        console.log(error);
    }
})