import React from 'react';
import './regist_style.css'
function regist_panel () {
    return (
        <div className='regist'>
            <h1>Добро пожаловать!</h1>
            <div className="btn-group">
                
                <a href="№" className="btn btn-primary">Зарегистрироваться</a>
                <a href='/login' className="btn btn-primary">Войти</a>
            </div>
        </div>
        
    );
}

export default regist_panel;