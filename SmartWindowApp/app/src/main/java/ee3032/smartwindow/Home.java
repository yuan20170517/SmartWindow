package ee3032.smartwindow;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.util.Log;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

import static ee3032.smartwindow.R.mipmap.window_closed;
import static ee3032.smartwindow.R.mipmap.window_open;

public class Home extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    public int open = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        // Firebase
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        final DatabaseReference openRef = database.getReference("opened");

        final ImageButton imageButton = (ImageButton) findViewById(R.id.imageButton);
        final TextView textWindow = (TextView) findViewById(R.id.textView2);


        // Check if window is open or closed
        openRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                open = Integer.parseInt(dataSnapshot.getValue(String.class));
                // Window is open
                if (open == 1) {
                    imageButton.setImageResource(window_open);
                    textWindow.setText("Window Open");
                }
                // Window is closed
                else {
                    imageButton.setImageResource(window_closed);
                    textWindow.setText("Window Closed");
                }
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Failed to read value
            }
        });

        // Button to open/close window
        imageButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Open window
                if (open == 0) {
                    open = 1;
                    openRef.setValue("1");
                    imageButton.setImageResource(window_open);
                    textWindow.setText("Window Open");
                }
                // Close window
                else {
                    open = 0;
                    openRef.setValue("0");
                    imageButton.setImageResource(window_closed);
                    textWindow.setText("Window Closed");
                }
            }
        });

        // Navigation Drawer
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
        navigationView.getMenu().getItem(0).setChecked(true);
        setTitle("Home");
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        item.setChecked(true);
        int id = item.getItemId();

        if (id == R.id.nav_home) {

        } else if (id == R.id.nav_control) {

        } else if (id == R.id.nav_camera) {
            startActivity(new Intent(Home.this, Camera.class).addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP));
        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
