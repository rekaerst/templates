#include <GL/glut.h> // glut, include glu.h gl.h

void drawQuad8f(float ax, float ay, float bx, float by, float cx, float cy,
				float dx, float dy) {
	glBegin(GL_QUADS);
	glVertex2f(ax, ay);
	glVertex2f(bx, by);
	glVertex2f(cx, cy);
	glVertex2f(dx, dy);
	glEnd();
}

void initGL() {
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Set background color to black
}

/* Handler for window re-size event. Called back when the window first appears and
whenever the window is re-sized with its new width and height */
void reshape(GLsizei width, GLsizei height) { // GLsizei for non-negative integer
	// Compute aspect ratio of the new window
	if (height == 0)
		height = 1;
	// To prevent divide by 0
	GLfloat aspect = (GLfloat)width / (GLfloat)height;
	// Set the viewport to cover the new window
	glViewport(0, 0, width, height);
	// Set the aspect ratio of the clipping area to match the viewport
	glMatrixMode(GL_PROJECTION); // To operate on the Projection matrix
	glLoadIdentity();
	// Reset the projection matrix
	if (width >= height) {
		// aspect >= 1, set the height from -1 to 1, with larger width
		gluOrtho2D(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0);
	} else {
		// aspect < 1, set the width to -1 to 1, with larger height
		gluOrtho2D(-1.0, 1.0, -1.0 / aspect, 1.0 / aspect);
	}
}
// repaint handler, a callback function
void display() {
	glClear(GL_COLOR_BUFFER_BIT); // Clear the color buffer

	static const float cube_len = 0.8f;
	static const float pro_factor = 0.75f; // projection factor
	static const float cos_30 = 0.866025404f;
	// Draw a Red Square
	glColor3f(1.0f, 0.0f, 0.0f);
	drawQuad8f(0.0f, 0.0f, 0.0f, -cube_len, cube_len * pro_factor * cos_30,
			   -cube_len * pro_factor / 2, cube_len * cos_30, cube_len / 2);
	glColor3f(0.0f, 1.0f, 0.0f);
	drawQuad8f(0.0f, 0.0f, 0.0f, -cube_len, -cube_len * pro_factor * cos_30,
			   -cube_len * pro_factor / 2, -cube_len * cos_30, cube_len / 2);
	glColor3f(0.0f, 0.0f, 1.0f);
	drawQuad8f(0.0f, 0.0f, -cube_len * cos_30, cube_len / 2, 0, pro_factor * cube_len, cube_len * cos_30, cube_len / 2);

	glFlush(); // Render now
}

int main(int argc, char** argv) {
	glutInit(&argc, argv); // Initialize GLUT
	glutInitWindowSize(320, 320); // Set initial width & height of the window
	glutCreateWindow("OpenGL Template"); // Create window with given title
	glutDisplayFunc(display); // Register display callback handler for window repaint
	glutReshapeFunc(reshape);
	initGL();
	glutMainLoop(); // Enter the event processing loop
	return 0;
}
