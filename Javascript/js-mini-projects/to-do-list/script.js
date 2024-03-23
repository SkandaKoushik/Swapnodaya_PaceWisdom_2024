function add_item() {
    let item = document.getElementById('box');
    let item_list = document.getElementById('item-list');

    if(item.value != '') {
        let make_li = document.createElement('li');
        make_li.appendChild(document.createTextNode(item.value));
        item_list.appendChild(make_li);
        item.value = '';

        make_li.ondblclick = function(){
            this.parentNode.removeChild(this);
        }
    }
    else {
        alert('Please add a value to item');
    }
}