#Jeffrey Carson & Grace Meredith

Changes made to code:

We looked over ur code and found that it already followed many good code design principles, specifically the fact that it was quite modular. Therefore, we spent time finding and removing bugs and covering edge cases. However, we had to include more return statements to fix said bugs, and this allowed us to more efficiently test our code and get more coverage. For instance, in the updateBoard() function, we now return true if the update was successful. We have also updated switchTurn(), and it now returns the current turn as a variable instead of updating the class attribute.

Tests:

test_GameOver()
	Condition Coverage
	Branch Coverage
	Function Coverage
	Statement Coverage
	Edge Coverage

test_UpdateBoard()
	Condition Coverage
	Branch Coverage
	Function Coverage
	Statement Coverage
	Edge Coverage

test_DisplayBoard()
	Function Coverage

test_switchTurn()
	Branch Coverage
	Conditional Coverage

Total Coverage: 75% (using coverage.py)