$(document).ready(function () {
  const element = "<li>Item</li>";

  $('#add_element').click(function () {
    $('.my_list').append(element);
  });

  $('#remove_element').click(function () {
    $('li:last').remove();
  });

  $('#clear_list').click(function () {
    $('ul').empty();
  });
});
