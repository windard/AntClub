$(function(){  
    //当滚动条的位置处于距顶部 300 像素以下时，跳转链接出现，否则消失  
    $(function () {  
        $(window).scroll(function(){  
            if ($(window).scrollTop() > 300){  
                $("#back-to-top").fadeIn(300);  
            }  
            else  
            {  
                $("#back-to-top").fadeOut(300);  
            }  
        });  

        //当点击跳转链接后，回到页面顶部位置  

        $("#back-to-top").click(function(){  
            $('body,html').animate({scrollTop:0},1000);  
            return false;  
        });  
    });  
}); 
$(function(){
    var $timeline_block = $('.timeline-block');
    //hide timeline blocks which are outside the viewport
    $timeline_block.each(function(){
        if($(this).offset().top > $(window).scrollTop()+$(window).height()*0.75) {
            $(this).find('.timeline-pic').addClass('is-hidden');
            $(this).find('.timeline-content').addClass('is-hidden');
        }
    });
    //on scolling, show/animate timeline blocks when enter the viewport
    $(window).on('scroll', function(){
        $timeline_block.each(function(){
            if( $(this).offset().top <= $(window).scrollTop()+$(window).height()*0.75 && $(this).find('.timeline-pic').hasClass('is-hidden') ) {
                $(this).find('.timeline-pic').removeClass('is-hidden').addClass('bounce-in');
                $(this).find('.timeline-content').removeClass('is-hidden').addClass('bounce-in');
            }
        });
    });
});