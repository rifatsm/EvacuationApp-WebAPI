package com.example.tahmi.evacuationapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class TriggerActivity extends AppCompatActivity {

    TextView text;
    TextView text2;
    Button button;
    Button button2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_trigger);

        text = (TextView) findViewById(R.id.textView4);
        button = (Button) findViewById(R.id.custom_button);

        text2 = (TextView) findViewById(R.id.textView5);
        button2 = (Button) findViewById(R.id.button2);


        button.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v) {
                text.setText("Alert Sent To Admin");

            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                text2.setText("Alert Discarded By Admin.");
            }
        });

    }
}
