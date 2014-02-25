function isalnum(str){
        var reg=/^[0-9a-zA-Z]{6,20}$/;
        return reg.test(str);
}
$(function(){
	var ok2=false;
	var ok3=false;
	//验证密码
	$('input[name="newpw"]').focus(function(){
		if($(this).val()==''){ok2=false;$(this).next().text('此项为必填');}
    	else if(!isalnum($(this).val())){
    		ok2=false;
			$(this).next().text('密码应在6-20位之间,只包含数字与字母');
        	$('#newpw').addClass('error');
        }
    	else if(isalnum($(this).val())&&$(this).val()!=''){
			$(this).next().text('');
			ok2=true;
            $('#newpw').removeClass('error');
		}
	}).blur(function(){
		if($(this).val()==''){ok2=false;$(this).next().text('此项为必填');}
    	else if(!isalnum($(this).val())){
    		ok2=false;
			$(this).next().text('密码应在6-20位之间,只包含数字与字母');
        	$('#newpw').addClass('error');
        }
    	else if(isalnum($(this).val())&&$(this).val()!=''){
			$(this).next().text('');
			ok2=true;
            $('#newpw').removeClass('error');
		}
	});

	//验证确认密码
	$('input[name="newpw2"]').focus(function(){
    	if($(this).val() != $('input[name="newpw"]').val()){
			$(this).next().text('输入的确认密码要与上面一致');
            $('#newpw2').addClass('error');
            ok3=false;
        }
        else{
        	ok3=true;
        	$('#newpw2').removeClass('error');
        }
	}).blur(function(){
		if($(this).val() == $('input[name="newpw"]').val()){
			$(this).next().text('');
			ok3=true;
            $('#newpw2').removeClass('error');
		}else{
			ok3=false;
			$(this).next().text('输入的确认密码要与上面一致');
            $('#newpw2').addClass('error');
		}
					
	});

	$('#setsummit').click(function(){
			if(ok2 && ok3){
				$('#settingbox').submit();
			}
			else{
				return false;
			}
	});
      
});