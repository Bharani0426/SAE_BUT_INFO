package Code;

import java.util.ArrayList;

import ardoise.*;
public class GF extends Forme {
	
	private ArrayList<Forme> formes;
	private ArrayList<Segment> segments;
	
	public GF(ArrayList<Forme> f) {
		segments=new ArrayList<Segment>();
		this.formes=f;
		for (int j=0;j<f.size();j++)
		{
			for (int i=0;i<f.get(j).dessiner().size();i++)
			{
				segments.add(f.get(j).dessiner().get(i));
			}
		}
	}
	
	@Override
	public void deplacer(int arg0, int arg1) {
		for (int j=0;j<formes.size();j++)
		{
			for (int i=0;i<formes.size();i++)
			{
				formes.get(j).dessiner().get(i).deplacer(arg0, arg1);
			}
		}
	}

	@SuppressWarnings("null")
	@Override
	public ArrayList<Segment> dessiner() {
		ArrayList<Segment> totale = new ArrayList<Segment>();
		for (int i=0;i<formes.size();i++)
		{
			totale.addAll(formes.get(i).dessiner());
		}
		return totale;
	}

	@Override
	public String typeForme()
	{
		return "GF";
	}

}