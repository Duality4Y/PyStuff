#include "SDL/SDL.h"
#include "SDL/SDL_image.h"
#include <string>

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;
const int SCREEN_BPP = 32;

SDL_Surface *image = NULL;
SDL_Surface *screen = NULL;

SDL_Event event;

SDL_Surface *load_image(std::string filename){
	//the image that's loaded;
	SDL_Surface* loadedImage = NULL;
	//the optimized image that will be used;
	SDL_Surface* optimizedImage = NULL;
	//load the image;
	loadedImage = IMG_Load(filename.c_str());
	//if the image loaded
	if(loadedImage!=NULL){
		//create and optimized image
		optimizedImage = SDL_DisplayFormat(loadedImage);
		//free the old image;
		SDL_FreeSurface(loadedImage);
	}
	//return the optimized image;
	return optimizedImage;
}

void apply_surface(int x, int y, SDL_Surface* source, SDL_Surface* destination){
	//temporary rectable to hold the offsets;
	SDL_Rect offset;
	//get the ofsets
	offset.x = x;
	offset.y = y;
	//blit the surface
	SDL_BlitSurface(source, NULL, destination, &offset):
}

bool init(){
	//initialize all sdl subsystems
	if(SDL_Init(SDL_INIT_EVERYTHING)==-1){
		return false;
	}
	//set up the screen;
	screen == SDL_SetVideoMode(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BPP, SDL_SWSURFACE);
	//if there was an error in settin up the screen.
	if(screen == NULL){
		return false;
	}
	//set the window caption
	SDL_WM_SetCaption("event test", NULL);
	//if everything initialized fine.
	return true;
}

bool load_files(){
	//load the image
	image = load_image("x.png");
	//if there was an error in loading the image
	if(image==NULL){
		return false;
	}
	//if everything loaded fine.
	return true;
}

void clean_up(){
	//free the image;
	SDL_FreeSurface(image);
	//quit sdl;
	SDL_Quit();
}

int main(int argc, char* args[]){
	//make sure the program waits for a quit;
	bool quit = false;
	//initialize;
	if(init()==false){
		return 1;
	}
	//load the files
	if(load_files()==false){
		return 1;
	}
	//apply the surface to the screen
	apply_surface(0,0,image,screen);
	//update the screen
	if(SDL_Flip(screen)==-1){
		return 1;
	}
	//while the user hasn't quit
	while(quit==false){
		while(SDL_PollEvent(&event)){
			//if the user has Xed out the window
			if(event.type == SDL_QUIT){
				//quit the program
				quit = true;
			}
		}
	}
	//free the surface and quit SDL
	clean_up();
	return 0;
}
