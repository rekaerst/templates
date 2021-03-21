#include <GL/glut.h>  // glut, include glu.h gl.h

void drawQuad8f(float ax, float ay, float bx, float by, float cx, float cy,
                float dx, float dy) {
  glBegin(GL_QUADS);
  glVertex2f(ax, ay);
  glVertex2f(bx, by);
  glVertex2f(cx, cy);
  glVertex2f(dx, dy);
  glEnd();
}
// repaint handler, a callback function
void display() {
  glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // Set background color to black
  glClear(GL_COLOR_BUFFER_BIT);          // Clear the color buffer

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
  drawQuad8f(0.0f, 0.0f, -cube_len * cos_30, cube_len / 2,0,pro_factor * cube_len, cube_len * cos_30, cube_len / 2);

  glFlush();  // Render now
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);                // Initialize GLUT
  glutCreateWindow("OpenGL Template");  // Create window with given title
  glutInitWindowSize(320, 320);  // Set initial width & height of the window
  glutDisplayFunc(
      display);    // Register display callback handler for window repaint
  glutMainLoop();  // Enter the event processing loop
  return 0;
}
