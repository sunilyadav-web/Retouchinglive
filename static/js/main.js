
// =========== CHANGE BACKGROUND HEADER ================

function scrollHeader() {
  const nav = document.getElementById("header");
  if (this.scrollY >= 80)
    nav.classList.add("scroll-header");
  else
    nav.classList.remove("scroll-header");
}
window.addEventListener('scroll', scrollHeader)


//=================== Password Hide and show====================
var state = false
function showpass() {
  var pass = document.getElementById('pass')
  var eye = document.getElementById('eye')
  if (state) {
    pass.setAttribute("type", "password")
    state = false
    eye.classList.add('bx-show')
    eye.classList.remove('bxs-hide')

  } else {
    pass.setAttribute("type", "text")
    state = true
    eye.classList.add('bxs-hide')
    eye.classList.remove('bx-show')
  }
}

// ================ Submit Form ==============

const myform = document.getElementById('form')
myform.addEventListener('submit', e => {
  e.preventDefault()

  $.ajax({
    type: 'POST',
    url: 'send-data',
    data: {
      name: $('#name').val(),
      phone: $('#phone').val(),
      email: $('#email').val(),
      query: $('#query').val(),
      msg: $('#msg').val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    success: function (data) {
      document.getElementById('parent-alert').classList.remove('d-none')
      document.getElementById('alert').innerHTML=data
      var input=document.querySelectorAll('.contact__form-input')
      input.forEach(data=>{
        data.value=''
      })
    }
  })
})

// =========== Scroll Page on click ==================

window.onload = function () {
  url = window.location.href
  surl = url.split("/")
  u = surl.slice(-1)
  if (u == 'services') {
    window.scroll(0, 1274)
  } else if (u == 'our-work') {
    window.scroll(0, 1739)
  } else if (u == 'contact') {
    window.scroll(0, 2372)
  }
  else if (u == 'home') {
    window.scroll(0, 0)
  }
}

// ============ Get Current Year =============

window.onload=function(){
  const d = new Date();
  let year = d.getFullYear();
  document.getElementById("year").innerHTML = year;
}