(function($){
  $.fn.asDeleteButton = function(){

    var csrftoken = getCookie('csrftoken');
    $.each(this,function(idx,dom_object){
      var button = $(dom_object);
      var parrent_card = button.closest('div.card');
      console.log( button.attr('href'));

      button.on('click',function(e){
        e.preventDefault();
        $.ajax({
          url : button.attr('href'),
          type : "POST",
          dataType: 'html'
        })
        .fail(function(xhr){
          //deletion failed
          console.log(xhr);
        })
        .done(function(data){
          //deletion complete
        });
        return 0;
      });

    });
  };
}(jQuery));
