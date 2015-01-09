import matplotlib.pyplot as plt
from numpy import *
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
	sys.stderr.write("Usage: python eval.py <prediction.txt> <answer.txt>\n" )
        sys.exit(0)

    predict = open( sys.argv[1] , 'r' )
    answers = open( sys.argv[2] , 'r' )

    correct = 0
    predict_count = 0
    answer_count = 0
    line_count = 0
    plt_x = []
    plt_y = []

    while True:
        pre_line = predict.readline()
	ans_line = answers.readline()
	line_count += 1
	exit = False
	if not pre_line:
	    sys.stderr.write("EOF for " + sys.argv[1] + "\n" );
	    exit = True
	if not ans_line:
	    sys.stderr.write("EOF for " + sys.argv[2] + "\n" );
	    exit = True
	if exit:
	    break
    
    	predictions = pre_line.rstrip("\n").split() 
	adopters    = ans_line.rstrip("\n").split() 
	#print predictions
	predict_count += len(predictions)
	answer_count += len(adopters)

	idea_correct = 0
        y = empty(len(predictions))
#plt_y = zeros((len(predictions), 1))
#sys.stdout.write("%d" % (line_count) )
	for i in range(len(predictions) ):
	    if predictions[i] in adopters:
		correct += 1
		idea_correct += 1
	    k_precision = float(idea_correct) / float(i + 1)
#sys.stdout.write(" %4f" % (k_precision) )
            y[i] = k_precision
#sys.stdout.write( "\n")
        plt_x.append(arange(1, len(predictions)+1))
        plt_y.append(y)

    try: 
       fig = plt.figure();
       if hasattr(fig, "show"):
           for i in range(len(plt_x)):
               plt.plot(plt_x[i], plt_y[i])

           plt.ylim(0, 1.1)
           plt.xlabel("# of data") 
           plt.ylabel("precision") 
           plt.title("The Title") 
       
    except:
       print "no display"

    precision = float(correct)/float(predict_count) 
    print( "precision = %d / %d , %4f" %( correct, predict_count, precision ) )
    recall = float(correct)/float(answer_count) 
    print( "recall    = %d / %d , %4f" %( correct, answer_count, recall ) )
    f_measure = 2.0 / ((1.0/precision) + (1.0/recall) )
    print( "f-measure = %4f" %( f_measure ) )

