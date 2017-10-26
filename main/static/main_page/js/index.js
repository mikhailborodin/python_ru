$('button.more-button').on('click', function(){
  var next_page = $('.pagination li.active').next().find('a').text();
  if (next_page){
    $.ajax({
      url: 'http://localhost:8000/api/cards/' + next_page
    }).done(function(response){
      var landing = '<div class="landing"><div class="row">';
      $.each(response.data, function(index, element){
        index += 1;
        landing += '\
          <div class="col-md-4 col-sm-6 article card">\
          <p class="img-container"><img src="' + element.image + '" class="img-responsive" height="180" width="300"></p>\
          <p class="tag"><a href="#">' + element.title + '</a></p>\
          <h4><a href="' + element.url + '">' + element.title + '</a></h4>\
          <p class="text">' + element.preview + '</p>'
        if (element.has_button){
          landing += '<a href="' + element.button_url + '" class="btn btn-square">'+ element.button_text + '</a></div>'
        } else {
          landing += '<p class="date">3 дня назад</p></div>'
        }
        if (index % 3 === 0){
          landing += '<div class="col-md-12 hidden-sm hidden-xs"></div>'
        }
        if (index % 2 === 0){
          landing += '<div class="col-sm-12 hidden-md hidden-lg hidden-xs"></div>'
        }
      })
      landing += '</div></div>'
      $('.landing').last().after(landing);
    });
  }
})