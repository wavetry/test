#version 330 core 
out vec4 FragColor;

in vec4 vertexColor;
uniform vec4 ourColor;
float timeValue = glfwGetTime();
float greenValue = (sin(timeValue) / 2.0f) + 0.5f;
int vertexColorLocation = glGetUniformLocation(shaderPorgram,"ourColor");
glUseProgram(shaderProgram);
glUniform4f(vertexColorLocation,0.0f,greenValue,0.0f,1.0f);


void main()
{
	FragColor = vertexColor;
	FragColor = ourColor;
}