#include <gtk/gtk.h>
#include <math.h>
#include <stdbool.h>

/* Quit application */
void quit (GtkWidget* widget, gpointer data)
{
    g_application_quit(G_APPLICATION(data));
}


/* Activate function, for initializing GUI
 * note that gpointer is just a null pointer */
static void activate(GtkApplication* app, gpointer data) {
	GtkCssProvider* provider = gtk_css_provider_new();
	// Note that a common practices is to declare all widgets as GtkWidget*
	// and use type cast when need to specific widget type.
	GtkWidget* window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	GtkWidget* textview = gtk_text_view_new();
	GtkWidget* quit_btn = gtk_button_new_with_label("Quit");
	// Create a horizontal box for packing widgets, second parameter is margin between widgets
	GtkWidget* hbox = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 8);
	GtkTextBuffer* textview_buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(textview));

	const char* greeting = "Hello World!";
	const char* window_title = "greeting";

	// Set application style to the style defined in ./style.css
	gtk_css_provider_load_from_path(provider, "style.css", NULL);
	gtk_style_context_add_provider_for_screen(gdk_screen_get_default(), GTK_STYLE_PROVIDER(provider), GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);

	// Set window as main window of your application
	gtk_window_set_application(GTK_WINDOW(window), app);
	gtk_window_set_title(GTK_WINDOW(window), window_title);
	gtk_window_set_default_size(GTK_WINDOW(window), 320, 60);

	// Set margins around the box
	gtk_widget_set_margin_top(hbox, 16);
	gtk_widget_set_margin_bottom(hbox, 16);
	// Set left and right margin if your are not from the Arabic
	gtk_widget_set_margin_start(hbox, 16);
	gtk_widget_set_margin_end(hbox, 16);

	// Request the minimum size of textview
	gtk_widget_set_size_request(textview, 200, 20);
	gtk_text_view_set_editable(GTK_TEXT_VIEW(textview),FALSE);
	gtk_text_buffer_set_text(GTK_TEXT_BUFFER(textview_buffer), greeting, strlen(greeting));
	// Use gtk_box_pack_start to pack your widget from the start of the box
	gtk_box_pack_start(GTK_BOX(hbox), textview, TRUE, TRUE, 8);

	// Connect button signals, which was generated after clicked the button,
	// to a callback function that quit current application
	g_signal_connect(quit_btn, "clicked", G_CALLBACK(quit), app);
	gtk_box_pack_start(GTK_BOX(hbox), quit_btn, TRUE, TRUE, 8);

	// Use gtk_container_add function to add one widget into another
	gtk_container_add(GTK_CONTAINER(window), hbox);

	// Show window and all widgets on window
	gtk_widget_set_visible(window, TRUE);
	gtk_widget_show_all(window);
}

int main(int argc, char** argv) {
	GtkApplication* app;
	int status;

	// Create application
	app = gtk_application_new("com.yourname.yourapp", G_APPLICATION_FLAGS_NONE);
	// Gtk will call activate function when app starts
	g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
	// Run the app and get status
	status = g_application_run(G_APPLICATION(app), argc, argv);
	// Clean up
	g_object_unref(app);

	return status;
}
