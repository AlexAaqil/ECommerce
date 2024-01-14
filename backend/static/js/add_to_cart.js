//Add to cart

$("#add_to_cart_btn").on("click", function(){
    let quantity = $("#product_quantity").val();
    let product_id = $("#product_id").val();
    let product_title = $("#product_title").val();
    let product_price = $("#current_product_price").text(); // Fix: Corrected the selector
    let this_val = $(this);

    $.ajax({
        url: '/add_to_cart',
        data: {
            'id' : product_id,
            'quantity' : quantity,
            'title' : product_title,
            'price' : product_price,
        },
        datatype: 'json',
        beforeSend: function(){
            console.log("Adding Products to Cart...")
        },
        success: function(res){
            this_val.html("Item added to Cart")
            console.log("Added Products to Cart");
            $(".cart_items_count").text(response.total_cart_items)
        }
    })
});



