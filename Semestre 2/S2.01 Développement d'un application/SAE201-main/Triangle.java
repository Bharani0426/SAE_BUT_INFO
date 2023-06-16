package Code;

import java.util.ArrayList;
import ardoise.*;

public class Triangle extends Forme {

	 private Segment segment1;
	    private Segment segment2;
	    private Segment segment3;

	    public Triangle( Segment seg1, Segment seg2, Segment seg3) {
	        this.segment1 = seg1;
	        this.segment2 = seg2;
	        this.segment3 = seg3;
	    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<>();
        segments.add(segment1);
        segments.add(segment2);
        segments.add(segment3);
        return segments;
    }

    @Override
    public String typeForme() {
        return "T";
    }

    @Override
    public void deplacer(int Pas_X, int Pas_Y) {
        segment1.getPointDepart().deplacer(Pas_X, Pas_Y);
        segment1.getPointArrivee().deplacer(Pas_X, Pas_Y);
        segment2.getPointDepart().deplacer(Pas_X, Pas_Y);
        segment2.getPointArrivee().deplacer(Pas_X, Pas_Y);
        segment3.getPointDepart().deplacer(Pas_X, Pas_Y);
        segment3.getPointArrivee().deplacer(Pas_X, Pas_Y);
    }

}
