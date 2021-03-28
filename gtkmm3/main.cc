#include <gtkmm.h>

class MyWindow : public Gtk::Window {
	Gtk::Paned paned;
	Gtk::Frame frame1, frame2;

public:
	MyWindow()
		: paned(Gtk::Orientation::ORIENTATION_VERTICAL) {
		set_title("Gtkmm Template");
		set_default_size(500, 300);
		set_border_width(10);
		add(paned);
		paned.add1(frame1);
		paned.add2(frame2);
		frame1.set_label("Gtk::Frame 1 Widget");
		frame2.set_label("Gtk::Frame 2 Widget");
		frame1.set_label_align(0.0, 0.25);
		frame2.set_label_align(1.0);
		frame1.set_shadow_type(Gtk::ShadowType::SHADOW_ETCHED_OUT);
		frame2.set_shadow_type(Gtk::ShadowType::SHADOW_ETCHED_IN);
		show_all_children();
	}

	~MyWindow() {
	}
};

int main(int argc, char* argv[]) {
	auto app = Gtk::Application::create(argc, argv, "com.rekaerst.template");

	MyWindow window;

	return app->run(window);
}
