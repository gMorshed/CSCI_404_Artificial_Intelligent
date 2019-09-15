import java.util.*;

/**
 * This is the AiPlayer class.  It simulates a minimax player for the max
 * connect four game.
 * The constructor essentially does nothing. 
 * 
 * @author james spargo
 *
 */

public class AiPlayer 
{
    /**
     * The constructor essentially does nothing except instantiate an
     * AiPlayer object.
     *
     */
      private int depth;
     private final int NUM_COLUMNS = 7;
     private final int POSITIVE_INFINITY = 100000000;
     private final int NEGATIVE_INFINITY = -100000000;
     private  int turn=-100;
    public AiPlayer(int d) 
    {
        depth = d; //got the depth of the search tree
    }

    /**
     * This method plays a piece randomly on the board
     * @param currentGame The GameBoard object that is currently being used to
     * play the game.
     * @return an integer indicating which column the AiPlayer would like
     * to play in.
     */
    public int findBestPlay( GameBoard currentGame ) 
    {
    int playChoice = 99;
    playChoice=MINIMAX(currentGame); //I will check to see if the move is valid at minimax algorithm with alpha bet    
	return playChoice;
    }
    
     private int MINIMAX(GameBoard currentGame){ //player 1 is Maximining and player 2 is minimizing
        int playChoice=99;
        this.turn=currentGame.getCurrentTurn();
        int alpha = NEGATIVE_INFINITY;
        int beta = POSITIVE_INFINITY; //here as a global value for the root,but will be local in the MAX_VALUE or MIN_VALUE function
        int value= NEGATIVE_INFINITY;
        for(int i=0; i <NUM_COLUMNS; i++) { //go through all the columns and see which one has the best value
            if(currentGame.isValidPlay(i) ) { //check to see if there is a valid play
                GameBoard potentialGame = new GameBoard(currentGame.getGameBoard()); //make the next gameboard where i will be next move 
                potentialGame.playPiece(i); 
                int v = MIN_VALUE(potentialGame,alpha,beta, this.depth);
//                potentialGame.printGameBoard();
//                System.out.println(v);
                if(v > value ){ //maximaization node, choose the higher reward column
                    playChoice = i;
                    value = v;
                    
                }
            }
        }
        return playChoice;
    }
    
    private int MAX_VALUE(GameBoard currentGame,int alpha, int beta, int d_level){
        if(currentGame.getPieceCount() == 42 || d_level == 0){ //we have maximum piece in the board or dpeth limit researched, get evaluation value 
            return evaluation_function(currentGame); //terminal test
        }
        int v = NEGATIVE_INFINITY;
        for(int i=0;i<NUM_COLUMNS; i++){
            if(currentGame.isValidPlay(i) ) {
                GameBoard potentialGame = new GameBoard(currentGame.getGameBoard());
                potentialGame.playPiece(i);
                v = Math.max(v, MIN_VALUE(potentialGame,alpha,beta, d_level-1));
                if(v>=beta) { //pruning
                	return v;
                }
                alpha = Math.max(alpha, v);
            }
        }
        return v;
    }
    
    
    private int MIN_VALUE(GameBoard currentGame,int alpha,int beta, int d_level){ //just the oppsite of MAX-VALUE
        if(currentGame.getPieceCount() == 42|| d_level == 0){ //we have maximam piece in the board, get utility value        	
            return evaluation_function(currentGame); //terminal test
        }
        int v = POSITIVE_INFINITY;
        for(int i=0;i<NUM_COLUMNS;i++){
            if(currentGame.isValidPlay(i) ){
                GameBoard potentialGame = new GameBoard(currentGame.getGameBoard());
                potentialGame.playPiece(i);
                v = Math.min(v,MAX_VALUE(potentialGame,alpha,beta, d_level-1));
                if(v <=alpha) { //pruning
                	return v;
                }
                beta = Math.min(beta, v);
            }
        }
        return v;
    }
    
    
    
    public int utility_function(GameBoard currentGame){
    	if(this.turn==1) {
    		return currentGame.getScore(this.turn)-currentGame.getScore(2);
    	}
    	else {
    		return currentGame.getScore(this.turn)-currentGame.getScore(1);
    	}
        
    }
    /**I researched to find good evaluation function.
     * this evaluation function and getThreeCount and getTwoCount function has been adopted from
     * http://web.media.mit.edu/~msaveski/projects/2009_connect-four.html
     * amd the research paper included in the project write up
     * @param currentGame
     * @return
     */
    public int evaluation_function(GameBoard currentGame){
    	if(this.turn==1) {
    		if(currentGame.getPieceCount() == 42) { //means we have a full house,,this values have been adopted from the research paper given in the project
    			if(currentGame.getScore(this.turn)-currentGame.getScore(2) > 0) { //winning
        			return POSITIVE_INFINITY;
        		}
    			else if(currentGame.getScore(this.turn)-currentGame.getScore(2) < 0) {
    				return NEGATIVE_INFINITY+1;//there can be cases where there is no good move,,all move lead to losing.  in that case I'll just make a move, so the value is not quiet -infinity. So that I can pick a move I add 1 for comparison
    			}
    			else {
    				return 0;
    			}
    		}
    		return (currentGame.getScore(this.turn)*100+ currentGame.getThreeCount(this.turn)*10+ currentGame.getTwoCount(this.turn)*4)-   (currentGame.getScore(2)*16+ currentGame.getThreeCount(2)*9+ currentGame.getTwoCount(2)*4);
    	}
    	else {
    		if(currentGame.getPieceCount() == 42) { //means we have a full house,,this values have been adopted from the research paper given in the project
    			if(currentGame.getScore(this.turn)-currentGame.getScore(1) > 0) { //winning
        			return POSITIVE_INFINITY;
        		}
    			else if(currentGame.getScore(this.turn)-currentGame.getScore(1) < 0) {
    				return NEGATIVE_INFINITY+1;
    			}
    			else { //draw
    				return 0;
    			}
    		}
    		return (currentGame.getScore(this.turn)*100+ currentGame.getThreeCount(this.turn)*10+ currentGame.getTwoCount(this.turn)*4)-   (currentGame.getScore(1)*16+ currentGame.getThreeCount(1)*9+ currentGame.getTwoCount(1)*4);
    	}
        
    }
    
}