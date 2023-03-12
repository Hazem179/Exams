const url = window.location.href

const examBox = document.getElementById('exam-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')

// let form = document.getElementById('exam-form');
// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     let formData = new FormData(form);
// })

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                examBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer => {
                    examBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
        });
        // activateTimer(response.time)

    },
    error: function (error) {
        console.log(error)
    }
})

const examForm = document.getElementById('exam-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')];
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;
    elements.forEach(element => {
        if (element.checked) {
            data[element.name] = element.value;
        } else {
            if (!data[element.name]) {
                data[element.name] = null;
            }
        }
    });
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }

    })

}

if (examForm) {
    examForm.addEventListener('submit', e => {
        e.preventDefault()
        sendData()
    })
}


