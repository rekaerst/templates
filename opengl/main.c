#include <GL/glut.h> // glut, include glu.h gl.h

// repaint handler, a callback function
void display() {
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Set background color to black
	glClear(GL_COLOR_BUFFER_BIT); // Clear the color buffer

	// Draw a Red Square
	glBegin(GL_QUADS); // Each set of 4 vertices form a quad
	glColor3f(1.0f, 0.0f, 0.0f);
	glVertex2f(-0.5f, -0.5f);
	glVertex2f(0.5f, -0.5f);
	glVertex2f(0.5f, 0.5f);
	glVertex2f(-0.5f, 0.5f);
	glEnd();

	glFlush(); // Render now
}

int main(int argc, char** argv) {
	glutInit(&argc, argv); // Initialize GLUT
	glutCreateWindow("OpenGL Template"); // Create window with given title
	glutInitWindowSize(320, 320); // Set initial width & height of the window
	glutDisplayFunc(display); // Register display callback handler for window repaint
	glutMainLoop(); // Enter the event processing loop
	return 0;
}
