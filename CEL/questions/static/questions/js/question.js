function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', ()=> {
    const questions = Object.values({{questions|safe}});
    // console.log("{{questions}}");
    console.log(questions);

    load_question(1);

    document.querySelectorAll('.navigation-circles').forEach( (circle) => {
        circle.onclick = ()=> {
            var question_number = circle.innerHTML;
            load_question(question_number)
        };
    });

    function load_question(question_number) {
        current_question = questions[question_number - 1];
        console.log(current_question);

        var image_box = document.querySelector('.question-image');
        var form = document.querySelector('#question-form');

        // Adding Text
        document.querySelector('.question-text').innerHTML = question_number + " . " + current_question.question_text;
        
        // Adding Image
        if(current_question.question_image != "") {
            var image = document.createElement("img");
            image.src = "media\/" + current_question.question_image;
            image.setAttribute('class', 'rounded');
            image_box.innerHTML = "";
            image_box.append(image);
        }
        else {
            image_box.innerHTML = "";
        }

        // Adding Input field
        form.innerHTML = "";
        const csrftoken = getCookie('csrftoken');

        var csrf = document.createElement('input');
        csrf.setAttribute('type', 'hidden');
        csrf.setAttribute('name', 'csrfmiddlewaretoken');
        csrf.setAttribute('value', csrftoken);
        form.append(csrf); 
        // form.innerHTML = "{% csrf_token %}";

        var username = document.createElement('input');
        username.setAttribute('type', 'hidden');
        username.setAttribute('name', 'username');
        username.setAttribute('value', '{{request.user.username}}');
        form.append(username);

        var answer_no = document.createElement('input');
        answer_no.setAttribute('type', 'hidden');
        answer_no.setAttribute('name', 'answer_no');
        answer_no.setAttribute('value', question_number);
        form.append(answer_no);

        var type = document.createElement('input');
        type.setAttribute('type', 'hidden');
        type.setAttribute('name', 'type');
        

        if(current_question.answer_type == 1) {
            var text_input = document.createElement('input');
            text_input.setAttribute('type', 'text');
            text_input.setAttribute('name', 'answer');
            text_input.setAttribute('class', 'form-control mx-auto fields')
            form.append(text_input);

            type.setAttribute('value', 'string');
            form.append(type);   
        }   
        else if(current_question.answer_type == 2) {
            var textarea_input = document.createElement('textarea');
            textarea_input.setAttribute('class', 'form-control mx-auto')
            textarea_input.setAttribute('name', 'answer');
            form.append(textarea_input);
            type.setAttribute('value', 'textarea');
            form.append(type);
        }
        else {
            var file_input = document.createElement('input');
            file_input.setAttribute('type', 'file');
            file_input.setAttribute('name', 'answer');
            file_input.setAttribute('class', 'form-control center-mx')
            form.append(file_input);

            type.setAttribute('value', 'file');
            form.append(type);
        }

        // Adding Submit
        var button = document.createElement('button');
        button.setAttribute('class', 'btn submit-button center-mx');
        button.setAttribute('type', 'submit');
        button.innerHTML = "Submit";
        form.append(button);
    };
});