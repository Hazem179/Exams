const modalBtns = [...document.getElementsByClassName("modal-button")]
const modalBody = document.getElementById("modal-body-confirm")
const startBtn = document.getElementById("start-button")
const url = window.location.href
modalBtns.forEach(modalBtn => modalBtn.addEventListener("click", () => {
    const pk = modalBtn.getAttribute("data-pk")
    const name = modalBtn.getAttribute("data-name")
    const questions = modalBtn.getAttribute("data-questions")
    const duration = modalBtn.getAttribute("data-duration")


    modalBody.innerHTML = '<div class="h5 mb-3">' + name + '</div> ' +
        '<div class="text-muted">' +
        '<ul>' +
        '<li> عدد الاسألة: ' + questions + ' اسألة</li>' +
        '<li> المدة: ' + duration + ' دقيقة</li>' +
        '<li>يرجي العلم انه عند بداية الاختبار لا يمكنك الخروج الا بعد الانتهاء من الاسألة او انتهاء وقت الامتحان المقرر</li>'
    '</ul> </div>'
    startBtn.addEventListener("click", () => {
        window.location.href = url + pk
    })
}));


