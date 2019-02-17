package com.example.tahmi.evacuationapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class SignUpActivity extends AppCompatActivity {

    Button submit;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_panic);

//        submit = (Button) findViewById(R.id.submit);
//
//        submit.setOnClickListener(new View.OnClickListener()
//        {
//            public void onClick(View v) {
//                startActivity(new Intent(SignUpActivity.this, TriggerActivity.class));
//            }
//        });
    }
}
